# TreatSubAssembliesAsComponents Property (IInterferenceDetectionMgr)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~TreatSubAssembliesAsComponents`

Gets or sets whether to treat subassemblies as single components so that interferences between a sub-assembly's components are not reported.
Gets or sets whether to treat subassemblies as single components so that interferences between a sub-assembly's components are not reported.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property TreatSubAssembliesAsComponents As System.Boolean
```

```

Dim instance As IInterferenceDetectionMgr
Dim value As System.Boolean
 
instance.TreatSubAssembliesAsComponents = value
 
value = instance.TreatSubAssembliesAsComponents
```

```

System.bool TreatSubAssembliesAsComponents {get; set;}
```

```

property System.bool TreatSubAssembliesAsComponents {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to treat a sub-assembly's components as single, false to not

Remarks

Currently, the value set for this property:

- exists only while the InterferenceDetectionMgr object is in scope; i.e., setting this property is temporary.
- does not persist across SOLIDWORKS sessions.
- does not persist into the next invocation of interference detection in the user interface.

Example

[Run Interference Detection (C#)](Run_Interference_Detection_Example_CSharp.htm)  
[Run Interference Detection (VB.NET)](Run_Interference_Detection_Example_VBNET.htm)  
[Run Interference Detection (VBA)](Run_Interference_Detection_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IInterferenceDetectionMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr.md)  
[IInterferenceDetectionMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr_members.md)  
[IInterferenceDetectionMgr::NonInterferingComponentDisplay Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~NonInterferingComponentDisplay.md)  
[IInterferenceDetectionMgr::MakeInterferingPartsTransparent Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~MakeInterferingPartsTransparent.md)  
[IInterferenceDetectionMgr::IGetInterferenceComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~IGetInterferenceComponents.md)  
[IInterferenceDetectionMgr::GetInterferenceComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~GetInterferenceComponents.md)  
[IInterferenceDetectionMgr::GetInterferenceComponentCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~GetInterferenceComponentCount.md)  
[IInterference::GetComponentCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterference~GetComponentCount.md)  
[IInterference::IGetComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterference~IGetComponents.md)  
[IInterference::Components Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterference~Components.md)
