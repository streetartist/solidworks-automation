# IGetFeatures Method (IBody2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IGetFeatures`

Gets the features in this body in a multibody sheet metal part.
Gets the features in this body in a multibody sheet metal part.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetFeatures( _
   ByVal NumberOfFeatures As System.Integer _
) As Feature
```

```

Dim instance As IBody2
Dim NumberOfFeatures As System.Integer
Dim value As Feature
 
value = instance.IGetFeatures(NumberOfFeatures)
```

```

Feature IGetFeatures( 
   System.int NumberOfFeatures
)
```

```

Feature^ IGetFeatures( 
   System.int NumberOfFeatures
) 
```

#### Parameters

*NumberOfFeatures*
:   Number of features in this body in a multibody sheet metal part

#### Return Value

- in-process, unmanaged C++: Pointer to an array of [features](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md) in this body in a multibody sheet metal part
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Before calling this method, call [IBody2::GetFeatureCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetFeatureCount.md) to get NumberOfFeatures.

The features of a body in a multibody sheet metal part are located in the solid bodies folder in the FeatureManager design tree.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)  
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.md)  
[IBody2::GetFeatures Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetFeatures.md)  
[IBodyFolder Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder.md)  
[IBodyFolder::GetBodyCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder~GetBodyCount.md)  
[IBodyFolder::GetBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder~GetBodies.md)  
[IBodyFolder::IGetBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder~IGetBodies.md)
