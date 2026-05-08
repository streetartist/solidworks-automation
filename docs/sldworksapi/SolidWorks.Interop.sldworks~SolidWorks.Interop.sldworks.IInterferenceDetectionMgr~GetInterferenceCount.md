# GetInterferenceCount Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~GetInterferenceCount`

Calculates and gets the number of interferences.
Calculates and gets the number of interferences.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetInterferenceCount() As System.Integer
```

```

Dim instance As IInterferenceDetectionMgr
Dim value As System.Integer
 
value = instance.GetInterferenceCount()
```

```

System.int GetInterferenceCount()
```

```

System.int GetInterferenceCount(); 
```

#### Return Value

Number of interferences

Remarks

Call this method before calling [IInterferenceDetectionMgr::IGetInterferences](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~IGetInterferences.md) to determine the size of the array for the interferences.

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
[IInterferenceDetectionMgr::GetInterferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~GetInterferences.md)
