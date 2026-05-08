# SchemaDescription Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimXpertManager~SchemaDescription`

Gets the description of the DimXpert schema.
Gets the description of the DimXpert schema.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property SchemaDescription As System.String
```

```

Dim instance As IDimXpertManager
Dim value As System.String
 
instance.SchemaDescription = value
 
value = instance.SchemaDescription
```

```

System.string SchemaDescription {get; set;}
```

```

property System.String^ SchemaDescription {
   System.String^ get();
   void set (    System.String^ value);
}
```

#### Property Value

The description of the DimXpert schema

Remarks

This property corresponds to a Properties menu item when the right-mouse-button is clicked on a schema in the DimXpertManager tab.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDimXpertManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimXpertManager.md)  
[IDimXpertManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimXpertManager_members.md)
