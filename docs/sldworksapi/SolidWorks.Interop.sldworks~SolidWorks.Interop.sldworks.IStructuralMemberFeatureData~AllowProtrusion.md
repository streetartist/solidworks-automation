# AllowProtrusion Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~AllowProtrusion`

Gets or sets whether to allow protrusion.
Gets or sets whether to allow protrusion.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property AllowProtrusion As System.Boolean
```

```

Dim instance As IStructuralMemberFeatureData
Dim value As System.Boolean
 
instance.AllowProtrusion = value
 
value = instance.AllowProtrusion
```

```

System.bool AllowProtrusion {get; set;}
```

```

property System.bool AllowProtrusion {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to allow protrusion, false to not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IStructuralMemberFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData.md)  
[IStructuralMemberFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData_members.md)
