# GetComponentsTransformInterferenceCount Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~GetComponentsTransformInterferenceCount`

Calculates and gets the number of interfering components for the specified components and math transform.
Calculates and gets the number of interfering components for the specified components and math transform.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetComponentsTransformInterferenceCount( _
   ByVal NumOfComponent As System.Integer, _
   ByRef Component As Component2, _
   ByRef Transform As MathTransform _
) As System.Integer
```

```

Dim instance As IInterferenceDetectionMgr
Dim NumOfComponent As System.Integer
Dim Component As Component2
Dim Transform As MathTransform
Dim value As System.Integer
 
value = instance.GetComponentsTransformInterferenceCount(NumOfComponent, Component, Transform)
```

```

System.int GetComponentsTransformInterferenceCount( 
   System.int NumOfComponent,
   ref Component2 Component,
   ref MathTransform Transform
)
```

```

System.int GetComponentsTransformInterferenceCount( 
   System.int NumOfComponent,
   Component2^% Component,
   MathTransform^% Transform
) 
```

#### Parameters

*NumOfComponent*
:   Number of components in the Component array

*Component*
:   Array of [IComponent2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)s

*Transform*
:   [IMathTransform](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform.md)

#### Return Value

Number of interfering components

Remarks

Call this method before calling [IInterferenceDetectionMgr::IGetComponentsTransformInterference](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~IGetComponentsTransformInterference.md) to get the size of the array returned by that method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IInterferenceDetectionMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr.md)  
[IInterferenceDetectionMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr_members.md)  
[IInterferenceDetectionMgr::GetComponentsTransformInterferenceCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~GetComponentsTransformInterferenceCount.md)
