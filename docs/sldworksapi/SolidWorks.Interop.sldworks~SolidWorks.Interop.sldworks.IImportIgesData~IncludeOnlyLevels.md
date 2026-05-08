# IncludeOnlyLevels Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportIgesData~IncludeOnlyLevels`

Gets the levels (layers) to import.
Gets the levels (layers) to import.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property IncludeOnlyLevels As System.Object
```

```

Dim instance As IImportIgesData
Dim value As System.Object
 
value = instance.IncludeOnlyLevels
```

```

System.object IncludeOnlyLevels {get;}
```

```

property System.Object^ IncludeOnlyLevels {
   System.Object^ get();
}
```

#### Property Value

Array of longs or integers (see [Long vs. Integer](sldworksapiprogguide.chm::/overview/Long_vs_Integer.htm)) indicating the levels to import

Remarks

[IImportIgesData::IncludeAllLevels](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportIgesData~IncludeAllLevels.md) must be false to use this property.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IImportIgesData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportIgesData.md)  
[IImportIgesData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportIgesData_members.md)  
[IImportIgesData::ProcessByLevel Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportIgesData~ProcessByLevel.md)  
[IImportIgesData::SetLevels Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportIgesData~SetLevels.md)
