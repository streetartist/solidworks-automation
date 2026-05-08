# ISetPatternBodyArray Method (ICurveDrivenPatternFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~ISetPatternBodyArray`

Sets the list of seed bodies for this curve-driven pattern feature.
Sets the list of seed bodies for this curve-driven pattern feature.

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

Dim instance As ICurveDrivenPatternFeatureData
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
:   - in-process, unmanaged C++: Pointer to an array of seed [bodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md) of size BodyCount

    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICurveDrivenPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData.md)  
[ICurveDrivenPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData_members.md)  
[ICurveDrivenPatternFeatureData::GetPatternBodyCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~GetPatternBodyCount.md)  
[ICurveDrivenPatternFeatureData::IGetPatternBodyArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~IGetPatternBodyArray.md)  
[ICurveDrivenPatternFeatureData::PatternBodyArray Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~PatternBodyArray.md)  
[ICurveDrivenPatternFeatureData::BodyPattern Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~BodyPattern.md)
