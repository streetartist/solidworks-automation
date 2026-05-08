# AutomaticRebuild Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~AutomaticRebuild`

Gets or sets whether to automatically rebuild after modifications.
Gets or sets whether to automatically rebuild after modifications.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property AutomaticRebuild As System.Boolean
```

```

Dim instance As IEquationMgr
Dim value As System.Boolean
 
instance.AutomaticRebuild = value
 
value = instance.AutomaticRebuild
```

```

System.bool AutomaticRebuild {get; set;}
```

```

property System.bool AutomaticRebuild {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to automatically rebuild after modifications, false to not

Remarks

This property corresponds to the **Automatic rebuild** checkbox in the Manage Equations dialog.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IEquationMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr.md)  
[IEquationMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr_members.md)  
[IEquationMgr::Equation Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~Equation.md)
