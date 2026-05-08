# ISetBodiesToCombine Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICombineBodiesFeatureData~ISetBodiesToCombine`

Sets the bodies to combine.
Sets the bodies to combine.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub ISetBodiesToCombine( _
   ByVal NCount As System.Integer, _
   ByRef PBodiesToCombine As Body2 _
) 
```

```

Dim instance As ICombineBodiesFeatureData
Dim NCount As System.Integer
Dim PBodiesToCombine As Body2
 
instance.ISetBodiesToCombine(NCount, PBodiesToCombine)
```

```

void ISetBodiesToCombine( 
   System.int NCount,
   ref Body2 PBodiesToCombine
)
```

```

void ISetBodiesToCombine( 
   System.int NCount,
   Body2^% PBodiesToCombine
) 
```

#### Parameters

*NCount*
:   Number of bodies to combine

*PBodiesToCombine*
:   - in-process, unmanaged C++: Pointer to an array of [bodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)

    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICombineBodiesFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICombineBodiesFeatureData.md)  
[ICombineBodiesFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICombineBodiesFeatureData_members.md)  
[ICombineBodiesFeatureData::GetBodiesToCombineCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICombineBodiesFeatureData~GetBodiesToCombineCount.md)  
[ICombineBodiesFeatureData::IGetBodiesToCombine Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICombineBodiesFeatureData~IGetBodiesToCombine.md)  
[ICombineBodiesFeatureData::BodiesToCombine Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICombineBodiesFeatureData~BodiesToCombine.md)
