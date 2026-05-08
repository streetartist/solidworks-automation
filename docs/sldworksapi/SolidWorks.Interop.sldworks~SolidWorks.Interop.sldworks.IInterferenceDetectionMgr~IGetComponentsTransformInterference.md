# IGetComponentsTransformInterference Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~IGetComponentsTransformInterference`

Calculates and gets the interfering components for the specified components and math transform.
Calculates and gets the interfering components for the specified components and math transform.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetComponentsTransformInterference( _
   ByVal NumOfComponent As System.Integer, _
   ByRef Component As Component2, _
   ByRef Transform As MathTransform, _
   ByVal NumOfIntComponent As System.Integer, _
   ByRef InterferingComponent As Component2 _
) As System.Boolean
```

```

Dim instance As IInterferenceDetectionMgr
Dim NumOfComponent As System.Integer
Dim Component As Component2
Dim Transform As MathTransform
Dim NumOfIntComponent As System.Integer
Dim InterferingComponent As Component2
Dim value As System.Boolean
 
value = instance.IGetComponentsTransformInterference(NumOfComponent, Component, Transform, NumOfIntComponent, InterferingComponent)
```

```

System.bool IGetComponentsTransformInterference( 
   System.int NumOfComponent,
   ref Component2 Component,
   ref MathTransform Transform,
   System.int NumOfIntComponent,
   out Component2 InterferingComponent
)
```

```

System.bool IGetComponentsTransformInterference( 
   System.int NumOfComponent,
   Component2^% Component,
   MathTransform^% Transform,
   System.int NumOfIntComponent,
   [Out] Component2^ InterferingComponent
) 
```

#### Parameters

*NumOfComponent*
:   Number of components in array specified by Component

*Component*
:   - in-process, unmanaged C++: Pointer to an array of [components](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)

    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

*Transform*
:   [IMathTransform](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform.md)

*NumOfIntComponent*
:   Number of interfering components in array returned by this method (see **Remarks**)

*InterferingComponent*
:   - in-process, unmanaged C++: Pointer to an array of interfering [components](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)

    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

#### Return Value

True if successful, false if not

Remarks

Before calling this method, call [IInterferenceDetectionMgr::GetComponentsTransformInterferenceCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~GetComponentsTransformInterferenceCount.md) to populate NumOfIntComponent.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IInterferenceDetectionMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr.md)  
[IInterferenceDetectionMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr_members.md)  
[IInterferenceDetectionMgr::GetComponentsTransformInterference Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~GetComponentsTransformInterference.md)  
[IInterferenceDetectionMgr::CreateFastenersFolder Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~CreateFastenersFolder.md)  
[IInterferenceDetectionMgr::IgnoreHiddenBodies Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~IgnoreHiddenBodies.md)  
[IInterferenceDetectionMgr::IncludeMultibodyPartInterferences Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~IncludeMultibodyPartInterferences.md)  
[IInterferenceDetectionMgr::MakeInterferingPartsTransparent Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~MakeInterferingPartsTransparent.md)  
[IInterferenceDetectionMgr::NonInterferingComponentDisplay Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~NonInterferingComponentDisplay.md)  
[IInterferenceDetectionMgr::ShowIgnoredInterferences Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~ShowIgnoredInterferences.md)  
[IInterferenceDetectionMgr::TreatCoincidenceAsInterference Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~TreatCoincidenceAsInterference.md)  
[IInterferenceDetectionMgr::TreatSubAssembliesAsComponents Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~TreatSubAssembliesAsComponents.md)  
[IInterferenceDetectionMgr::IGetInterferenceComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~IGetInterferenceComponents.md)
