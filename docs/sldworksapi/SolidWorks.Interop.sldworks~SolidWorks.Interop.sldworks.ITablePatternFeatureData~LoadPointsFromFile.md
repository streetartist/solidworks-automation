# LoadPointsFromFile Method (ITablePatternFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~LoadPointsFromFile`

Loads the location points of the table-driven pattern from a *.sldptab file.
Loads the location points of the table-driven pattern from a \*.sldptab file.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function LoadPointsFromFile( _
   ByVal FileName As System.String _
) As System.Boolean
```

```

Dim instance As ITablePatternFeatureData
Dim FileName As System.String
Dim value As System.Boolean
 
value = instance.LoadPointsFromFile(FileName)
```

```

System.bool LoadPointsFromFile( 
   System.string FileName
)
```

```

System.bool LoadPointsFromFile( 
   System.String^ FileName
) 
```

#### Parameters

*FileName*
:   Name of the file with the table-driven pattern feature's point locations

#### Return Value

True if the file loads successfully, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITablePatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData.md)  
[ITablePatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData_members.md)  
[ITablePatternFeatureData::SavePointsToFile Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~SavePointsToFile.md)
