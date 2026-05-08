# DisplayZebraStripes Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~DisplayZebraStripes`

Gets or sets the zebra-line display state.
Gets or sets the zebra-line display state.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property DisplayZebraStripes As System.Boolean
```

```

Dim instance As IModelView
Dim value As System.Boolean
 
instance.DisplayZebraStripes = value
 
value = instance.DisplayZebraStripes
```

```

System.bool DisplayZebraStripes {get; set;}
```

```

property System.bool DisplayZebraStripes {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to display the zebra stripes, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView.md)  
[IModelView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView_members.md)
