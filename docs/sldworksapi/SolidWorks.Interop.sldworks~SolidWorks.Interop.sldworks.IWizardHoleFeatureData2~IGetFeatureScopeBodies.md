# IGetFeatureScopeBodies Method (IWizardHoleFeatureData2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~IGetFeatureScopeBodies`

Gets the solid bodies that the Hole Wizard feature affects in a multibody part.
Gets the solid bodies that the Hole Wizard feature affects in a multibody part.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetFeatureScopeBodies( _
   ByVal Count As System.Integer _
) As Body2
```

```

Dim instance As IWizardHoleFeatureData2
Dim Count As System.Integer
Dim value As Body2
 
value = instance.IGetFeatureScopeBodies(Count)
```

```

Body2 IGetFeatureScopeBodies( 
   System.int Count
)
```

```

Body2^ IGetFeatureScopeBodies( 
   System.int Count
) 
```

#### Parameters

*Count*
:   Number of solid bodies to affect

#### Return Value

- in-process, unmanaged C++: Pointer to an array of solid [bodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md) of size Count

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Before calling this method, call [IWizardHoleFeatureData2::GetFeatureScopeBodiesCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~GetFeatureScopeBodiesCount.md) to get Count.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IWizardHoleFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2.md)  
[IWizardHoleFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2_members.md)  
[IWizardHoleFeatureData2::ISetFeatureScopeBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~ISetFeatureScopeBodies.md)  
[IWizardHoleFeatureData2::AutoSelect Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~AutoSelect.md)  
[IWizardHoleFeatureData2::FeatureScope Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~FeatureScope.md)  
[IWizardHoleFeatureData2::FeatureScopeBodies Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~FeatureScopeBodies.md)
