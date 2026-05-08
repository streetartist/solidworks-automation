# SetComponentsAndTransforms Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~SetComponentsAndTransforms`

Sets the interfering components and their transforms.
Sets the interfering components and their transforms.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetComponentsAndTransforms( _
   ByVal ComponentList As System.Object, _
   ByVal TransformList As System.Object _
) As System.Integer
```

```

Dim instance As IInterferenceDetectionMgr
Dim ComponentList As System.Object
Dim TransformList As System.Object
Dim value As System.Integer
 
value = instance.SetComponentsAndTransforms(ComponentList, TransformList)
```

```

System.int SetComponentsAndTransforms( 
   System.object ComponentList,
   System.object TransformList
)
```

```

System.int SetComponentsAndTransforms( 
   System.Object^ ComponentList,
   System.Object^ TransformList
) 
```

#### Parameters

*ComponentList*
:   Array of interfering [components](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)

*TransformList*
:   Array of [transforms](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform.md)

#### Return Value

Status as defined by [swSetComponentsAndTransformsStatus\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSetComponentsAndTransformsStatus_e.html)

Remarks

You must pass in absolute transforms to this method.

If you want to transform a component incrementally before interference detection, then you must multiply that incremental transform by the component's existing transform before passing in the resultant transform.

To produce the effect of identity transforms on components (i.e., the components do not move while participating in interference detection), the transforms for those components passed in can be null or Nothing. However, passing in null or Nothing for all of the transforms is interpreted as invalid input.

**NOTE:** A null or Nothing is interpreted as the component’s existing transform (i.e., an identity incremental transform).

Example

[Set Components and Transforms for Interference Detection (C#)](Set_Components_and_Transforms_for_Interference_Detection_Example_CSharp.htm)  
[Set Components and Transforms for Interference Detection (VB.NET)](Set_Components_and_Transforms_for_Interference_Detection_Example_VBNET.htm)  
[Set Components and Transforms for Interference Detection (VBA)](Set_Components_and_Transforms_for_Interference_Detection_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IInterferenceDetectionMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr.md)  
[IInterferenceDetectionMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr_members.md)  
[IInterferenceDectectionMgr::GetComponentsAndTransforms Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~GetComponentsAndTransforms.md)
