# SavePointsToFile Method (ITablePatternFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~SavePointsToFile`

Saves the location of the table-driven pattern feature's points to a *.sldptab file.
Saves the location of the table-driven pattern feature's points to a \*.sldptab file.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SavePointsToFile( _
   ByVal FileName As System.String _
) As System.Boolean
```

```

Dim instance As ITablePatternFeatureData
Dim FileName As System.String
Dim value As System.Boolean
 
value = instance.SavePointsToFile(FileName)
```

```

System.bool SavePointsToFile( 
   System.string FileName
)
```

```

System.bool SavePointsToFile( 
   System.String^ FileName
) 
```

#### Parameters

*FileName*
:   Name of the file to which to save the points

#### Return Value

True if successful, false if not

Remarks

Exported units, e.g. meters, of the document that owns the feature, and not necessarily those of the active document, are used when data is saved to a file.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITablePatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData.md)  
[ITablePatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData_members.md)  
[ITablePatternFeatureData::LoadPointsFromFile Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~LoadPointsFromFile.md)
