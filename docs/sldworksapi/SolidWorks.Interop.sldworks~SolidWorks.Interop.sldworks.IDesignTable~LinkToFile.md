# LinkToFile Property (IDesignTable)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~LinkToFile`

Gets or sets whether to link the design table to the model.
Gets or sets whether to link the design table to the model.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property LinkToFile As System.Boolean
```

```

Dim instance As IDesignTable
Dim value As System.Boolean
 
instance.LinkToFile = value
 
value = instance.LinkToFile
```

```

System.bool LinkToFile {get; set;}
```

```

property System.bool LinkToFile {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to link the design table to the model, false to not

Remarks

When a design table is linked to the model, any changes you make to the design table outside of the SOLIDWORKS software are reflected in the design table within the SOLIDWORKS model, and vice versa.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDesignTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable.md)  
[IDesignTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable_members.md)  
[IDesignTable::FileName Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~FileName.md)  
[IDesignTable::SourceType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~SourceType.md)  
[IDesignTable::UpdateModel Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~UpdateModel.md)
