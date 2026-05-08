# IGetBodiesToCombine Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICombineBodiesFeatureData~IGetBodiesToCombine`

Gets the bodies to combine.
Gets the bodies to combine.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetBodiesToCombine( _
   ByVal NCount As System.Integer _
) As Body2
```

```

Dim instance As ICombineBodiesFeatureData
Dim NCount As System.Integer
Dim value As Body2
 
value = instance.IGetBodiesToCombine(NCount)
```

```

Body2 IGetBodiesToCombine( 
   System.int NCount
)
```

```

Body2^ IGetBodiesToCombine( 
   System.int NCount
) 
```

#### Parameters

*NCount*
:   Number of bodies to combine

#### Return Value

- in-process, unmanaged C++: Pointer to an array of [bodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Call [ICombineBodiesFeatureData::GetBodiesToCombineCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICombineBodiesFeatureData~GetBodiesToCombineCount.md) before calling this method to determine the size of the array.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICombineBodiesFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICombineBodiesFeatureData.md)  
[ICombineBodiesFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICombineBodiesFeatureData_members.md)  
[ICombineBodiesFeatureData::ISetBodiesToCombine Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICombineBodiesFeatureData~ISetBodiesToCombine.md)  
[ICombineBodiesFeatureData::BodiesToCombine Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICombineBodiesFeatureData~BodiesToCombine.md)
