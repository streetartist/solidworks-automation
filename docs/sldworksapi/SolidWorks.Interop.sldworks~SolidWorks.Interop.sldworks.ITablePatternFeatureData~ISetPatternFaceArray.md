# ISetPatternFaceArray Method (ITablePatternFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~ISetPatternFaceArray`

Sets the patterned faces for this table-driven pattern feature.
Sets the patterned faces for this table-driven pattern feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub ISetPatternFaceArray( _
   ByVal FaceCount As System.Integer, _
   ByRef ArrayDataIn As System.Object _
) 
```

```

Dim instance As ITablePatternFeatureData
Dim FaceCount As System.Integer
Dim ArrayDataIn As System.Object
 
instance.ISetPatternFaceArray(FaceCount, ArrayDataIn)
```

```

void ISetPatternFaceArray( 
   System.int FaceCount,
   ref System.object ArrayDataIn
)
```

```

void ISetPatternFaceArray( 
   System.int FaceCount,
   System.Object^% ArrayDataIn
) 
```

#### Parameters

*FaceCount*
:   Number of patterned faces

*ArrayDataIn*
:   - in-process, unmanaged C++: Pointer to an array of patterned [faces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)

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
[ITablePatternFeatureData::GetPatternFaceCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~GetPatternFaceCount.md)  
[ITablePatternFeatureData::IGetPatternFaceArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~IGetPatternFaceArray.md)  
[ITablePatternFeatureData::PatternFaceArray Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~PatternFaceArray.md)
