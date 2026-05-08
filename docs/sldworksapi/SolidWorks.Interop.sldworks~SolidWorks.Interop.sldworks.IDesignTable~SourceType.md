# SourceType Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~SourceType`

Gets or sets the type of source file for this design table.
Gets or sets the type of source file for this design table.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property SourceType As System.Integer
```

```

Dim instance As IDesignTable
Dim value As System.Integer
 
instance.SourceType = value
 
value = instance.SourceType
```

```

System.int SourceType {get; set;}
```

```

property System.int SourceType {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Type of source file as defined in [swDesignTableSourceTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDesignTableSourceTypes_e.html)

Remarks

You must call:

- [IDesignTable::EditFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~EditFeature.md) before setting this property.
- [IDesignTable::UpdateFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~UpdateFeature.md) after setting this property.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDesignTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable.md)  
[IDesignTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable_members.md)  
[IDesignTable::FileName Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~FileName.md)  
[IDesignTable::LinkToFile Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~LinkToFile.md)  
[IDesignTable::SaveAsExcelFile Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~SaveAsExcelFile.md)
