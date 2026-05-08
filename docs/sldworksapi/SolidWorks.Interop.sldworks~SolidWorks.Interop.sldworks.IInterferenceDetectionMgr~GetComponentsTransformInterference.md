# GetComponentsTransformInterference Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~GetComponentsTransformInterference`

Calculates and gets the interfering components for the specified components and math transform.
Calculates and gets the interfering components for the specified components and math transform.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetComponentsTransformInterference( _
   ByVal Component As System.Object, _
   ByVal Transform As System.Object, _
   ByRef InterferingComponent As System.Object _
) As System.Boolean
```

```

Dim instance As IInterferenceDetectionMgr
Dim Component As System.Object
Dim Transform As System.Object
Dim InterferingComponent As System.Object
Dim value As System.Boolean
 
value = instance.GetComponentsTransformInterference(Component, Transform, InterferingComponent)
```

```

System.bool GetComponentsTransformInterference( 
   System.object Component,
   System.object Transform,
   out System.object InterferingComponent
)
```

```

System.bool GetComponentsTransformInterference( 
   System.Object^ Component,
   System.Object^ Transform,
   [Out] System.Object^ InterferingComponent
) 
```

#### Parameters

*Component*
:   Array of [IComponent2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)s with which to detect interference

*Transform*
:   [IMathTransform](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform.md)

*InterferingComponent*
:   Array of interfering [IComponent2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)s

#### Return Value

True if successful, false if not

Example

[Detect Interferences Using a Transform (VBA)](Detect_Interferences_Using_a_Transform_Example_VB.htm)  
[Detect Interferences Using a Transform (VB.NET)](Detect_Interferences_Using_a_Transform_Example_VBNET.htm)  
[Detect Interferences Using a Transform (C#)](Detect_Interferences_Using_a_Transform_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IInterferenceDetectionMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr.md)  
[IInterferenceDetectionMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr_members.md)  
[IInterferenceDetectionMgr::IGetComponentsTransformInterference Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~IGetComponentsTransformInterference.md)  
[IInterferenceDetectionMgr::GetInterferenceComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~GetInterferenceComponents.md)  
[IInterferenceDetectionMgr::IGetInterferenceComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~IGetInterferenceComponents.md)  
[IInterferenceDetectionMgr::GetInterferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~GetInterferences.md)  
[IInterferenceDetectionMgr::IGetInterferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~IGetInterferences.md)  
[IInterferenceDetectionMgr::CreateFastenersFolder Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~CreateFastenersFolder.md)  
[IInterferenceDetectionMgr::IgnoreHiddenBodies Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~IgnoreHiddenBodies.md)  
[IInterferenceDetectionMgr::IncludeMultibodyPartInterferences Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~IncludeMultibodyPartInterferences.md)  
[IInterferenceDetectionMgr::MakeInterferingPartsTransparent Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~MakeInterferingPartsTransparent.md)  
[IInterferenceDetectionMgr::NonInterferingComponentDisplay Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~NonInterferingComponentDisplay.md)  
[IInterferenceDetectionMgr::ShowIgnoredInterferences Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~ShowIgnoredInterferences.md)  
[IInterferenceDetectionMgr::TreatCoincidenceAsInterference Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~TreatCoincidenceAsInterference.md)  
[IInterferenceDetectionMgr::TreatSubAssembliesAsComponents Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~TreatSubAssembliesAsComponents.md)  
[IInterferenceDetectionMgr::GetComponentsTransformInterferenceCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~GetComponentsTransformInterferenceCount.md)
