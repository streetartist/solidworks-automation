# ISetPatternFeatureArray Method (ITablePatternFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~ISetPatternFeatureArray`

Sets the seed features used to create the table-driven pattern feature.
Sets the seed features used to create the table-driven pattern feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub ISetPatternFeatureArray( _
   ByVal FeatCount As System.Integer, _
   ByRef ArrayDataIn As System.Object _
) 
```

```

Dim instance As ITablePatternFeatureData
Dim FeatCount As System.Integer
Dim ArrayDataIn As System.Object
 
instance.ISetPatternFeatureArray(FeatCount, ArrayDataIn)
```

```

void ISetPatternFeatureArray( 
   System.int FeatCount,
   ref System.object ArrayDataIn
)
```

```

void ISetPatternFeatureArray( 
   System.int FeatCount,
   System.Object^% ArrayDataIn
) 
```

#### Parameters

*FeatCount*
:   Number of seed features that to use to create this table-driven pattern feature

*ArrayDataIn*
:   - in-process, unmanaged C++: Pointer to an array of seed [features](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md) to use to create the table-driven pattern feature

    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITablePatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData.md)  
[ITablePatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData_members.md)  
[ITablePatternFeatureData::IGetPatternFeatureArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~IGetPatternFeatureArray.md)  
[ITablePatternFeatureData::PatternFeatureArray Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~PatternFeatureArray.md)  
[ITablePatternFeatureData::GetPatternFeatureCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~GetPatternFeatureCount.md)
