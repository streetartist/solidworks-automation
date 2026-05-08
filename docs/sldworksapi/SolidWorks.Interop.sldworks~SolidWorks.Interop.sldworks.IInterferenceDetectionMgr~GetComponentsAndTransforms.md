# GetComponentsAndTransforms Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~GetComponentsAndTransforms`

Gets the interfering components and their transforms.
Gets the interfering components and their transforms.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetComponentsAndTransforms( _
   ByRef ComponentList As System.Object, _
   ByRef TransformList As System.Object _
) As System.Boolean
```

```

Dim instance As IInterferenceDetectionMgr
Dim ComponentList As System.Object
Dim TransformList As System.Object
Dim value As System.Boolean
 
value = instance.GetComponentsAndTransforms(ComponentList, TransformList)
```

```

System.bool GetComponentsAndTransforms( 
   out System.object ComponentList,
   out System.object TransformList
)
```

```

System.bool GetComponentsAndTransforms( 
   [Out] System.Object^ ComponentList,
   [Out] System.Object^ TransformList
) 
```

#### Parameters

*ComponentList*
:   Array of interfering [components](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)

*TransformList*
:   Array of [transforms](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform.md)

#### Return Value

True if successful, false if not

Example

[Run Interference Detection (VBA)](Run_Interference_Detection_Example_VB.htm)  
[Run Interference Detection (VB.NET)](Run_Interference_Detection_Example_VBNET.htm)  
[Run Interference Detection (C#)](Run_Interference_Detection_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IInterferenceDetectionMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr.md)  
[IInterferenceDetectionMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr_members.md)  
[IInterferenceDectectionMgr::SetComponentsAndTransforms Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~SetComponentsAndTransforms.md)
