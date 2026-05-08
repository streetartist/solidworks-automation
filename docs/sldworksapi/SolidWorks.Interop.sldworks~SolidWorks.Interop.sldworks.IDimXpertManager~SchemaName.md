# SchemaName Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimXpertManager~SchemaName`

Gets the name of the DimXpertSchema.
Gets the name of the DimXpertSchema.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property SchemaName As System.String
```

```

Dim instance As IDimXpertManager
Dim value As System.String
 
instance.SchemaName = value
 
value = instance.SchemaName
```

```

System.string SchemaName {get; set;}
```

```

property System.String^ SchemaName {
   System.String^ get();
   void set (    System.String^ value);
}
```

#### Property Value

The name of the DimXpert schema

Remarks

This property corresponds to a Properties menu item when the right-mouse-button is clicked on a schema in the DimXpertManager tab.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDimXpertManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimXpertManager.md)  
[IDimXpertManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimXpertManager_members.md)
