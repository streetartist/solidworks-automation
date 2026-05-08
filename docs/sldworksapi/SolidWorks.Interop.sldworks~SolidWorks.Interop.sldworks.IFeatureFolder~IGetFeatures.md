# IGetFeatures Method (IFeatureFolder)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureFolder~IGetFeatures`

Gets the features in this feature folder.
Gets the features in this feature folder.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetFeatures( _
   ByVal NumOfFeatures As System.Integer _
) As Feature
```

```

Dim instance As IFeatureFolder
Dim NumOfFeatures As System.Integer
Dim value As Feature
 
value = instance.IGetFeatures(NumOfFeatures)
```

```

Feature IGetFeatures( 
   System.int NumOfFeatures
)
```

```

Feature^ IGetFeatures( 
   System.int NumOfFeatures
) 
```

#### Parameters

*NumOfFeatures*
:   Number of features in the folder

#### Return Value

- in-process, unmanaged C++: Pointer to an array of [features](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Before calling this method, call [IFeatureFolder::GetFeatureCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureFolder~GetFeatureCount.md) to populate NumOfFeatures.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureFolder Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureFolder.md)  
[IFeatureFolder Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureFolder_members.md)  
[IFeatureFolder::GetFeatures Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureFolder~GetFeatures.md)
