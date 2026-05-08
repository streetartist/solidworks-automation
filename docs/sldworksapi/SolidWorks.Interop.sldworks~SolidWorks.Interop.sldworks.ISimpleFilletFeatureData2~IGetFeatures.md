# IGetFeatures Method (ISimpleFilletFeatureData2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~IGetFeatures`

Gets the features on which to create a simple radius fillet.
Gets the features on which to create a simple radius fillet.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetFeatures( _
   ByVal Count As System.Integer _
) As Feature
```

```

Dim instance As ISimpleFilletFeatureData2
Dim Count As System.Integer
Dim value As Feature
 
value = instance.IGetFeatures(Count)
```

```

Feature IGetFeatures( 
   System.int Count
)
```

```

Feature^ IGetFeatures( 
   System.int Count
) 
```

#### Parameters

*Count*
:   Number of features

#### Return Value

- in-process, unmanaged C++: Pointer to an array of [features](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md) of size Count

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Call [ISimpleFilletFeatureData2::GetFeatureCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~GetFeatureCount.md) before calling this method to get the value for Count.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISimpleFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2.md)  
[ISimpleFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2_members.md)  
[ISimpleFilletFeatureData2::ISetFeatures Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~ISetFeatures.md)  
[ISimpleFilletFeatureData2::Features Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~Features.md)
