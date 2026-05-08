# ISetPatternBodyArray Method (IMirrorSolidFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorSolidFeatureData~ISetPatternBodyArray`

Sets the seed bodies for this mirror solid feature.
Sets the seed bodies for this mirror solid feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub ISetPatternBodyArray( _
   ByVal BodyCount As System.Integer, _
   ByRef ArrayDataIn As Body2 _
) 
```

```

Dim instance As IMirrorSolidFeatureData
Dim BodyCount As System.Integer
Dim ArrayDataIn As Body2
 
instance.ISetPatternBodyArray(BodyCount, ArrayDataIn)
```

```

void ISetPatternBodyArray( 
   System.int BodyCount,
   ref Body2 ArrayDataIn
)
```

```

void ISetPatternBodyArray( 
   System.int BodyCount,
   Body2^% ArrayDataIn
) 
```

#### Parameters

*BodyCount*
:   Number of seed bodies

*ArrayDataIn*
:   - in-process, unmanaged C++: Pointer to an array of seed [bodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)

    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMirrorSolidFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorSolidFeatureData.md)  
[IMirrorSolidFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorSolidFeatureData_members.md)  
[IMirrorSolidFeatureData::GetPatternBodyCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorSolidFeatureData~GetPatternBodyCount.md)  
[IMirrorSolidFeatureData::IGetPatternBodyArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorSolidFeatureData~IGetPatternBodyArray.md)  
[IMirrorSolidFeatureData::PatternBodyArray Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorSolidFeatureData~PatternBodyArray.md)
