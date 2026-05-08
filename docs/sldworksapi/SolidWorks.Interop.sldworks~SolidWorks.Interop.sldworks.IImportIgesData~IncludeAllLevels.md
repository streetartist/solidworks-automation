# IncludeAllLevels Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportIgesData~IncludeAllLevels`

Gets whether all levels (layers) are imported.
Gets whether all levels (layers) are imported.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property IncludeAllLevels As System.Boolean
```

```

Dim instance As IImportIgesData
Dim value As System.Boolean
 
value = instance.IncludeAllLevels
```

```

System.bool IncludeAllLevels {get;}
```

```

property System.bool IncludeAllLevels {
   System.bool get();
}
```

#### Property Value

True to import all levels, false to not

Remarks

If this property is false, then you can use [IImportIgesData::IncludeOnlyLevels](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportIgesData~IncludeOnlyLevels.md) to find out which levels will be processed.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IImportIgesData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportIgesData.md)  
[IImportIgesData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportIgesData_members.md)  
[IImportIgesData::ProcessByLevel Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportIgesData~ProcessByLevel.md)  
[IImportIgesData::SetLevels Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportIgesData~SetLevels.md)
