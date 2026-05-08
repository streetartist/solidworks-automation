# InterferenceDetectionManager Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~InterferenceDetectionManager`

Gets the Interference Detection manager, which allows you to run interference detection on an assembly to determine whether components interfere with each other.
Gets the Interference Detection manager, which allows you to run interference detection on an assembly to determine whether components interfere with each other.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property InterferenceDetectionManager As InterferenceDetectionMgr
```

```

Dim instance As IAssemblyDoc
Dim value As InterferenceDetectionMgr
 
value = instance.InterferenceDetectionManager
```

```

InterferenceDetectionMgr InterferenceDetectionManager {get;}
```

```

property InterferenceDetectionMgr^ InterferenceDetectionManager {
   InterferenceDetectionMgr^ get();
}
```

#### Property Value

[IInterferenceDetectionMgr](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr.md)

Example

[Run Interference Detection (C#)](Run_Interference_Detection_Example_CSharp.htm)  
[Run Interference Detection (VB.NET)](Run_Interference_Detection_Example_VBNET.htm)  
[Run Interference Detection (VBA)](Run_Interference_Detection_Example_VB.htm)  
[Detect Interferences Using a Transform (VBA)](Detect_Interferences_Using_a_Transform_Example_VB.htm)  
[Detect Interferences Using a Transform (VB.NET)](Detect_Interferences_Using_a_Transform_Example_VBNET.htm)  
[Detect Interferences Using a Transform (C#)](Detect_Interferences_Using_a_Transform_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.md)  
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.md)
