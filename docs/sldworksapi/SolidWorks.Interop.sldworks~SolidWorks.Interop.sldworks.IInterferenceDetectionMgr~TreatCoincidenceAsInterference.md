# TreatCoincidenceAsInterference Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~TreatCoincidenceAsInterference`

Gets or sets whether to treat coincident entities as interference.
Gets or sets whether to treat coincident entities as interference.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property TreatCoincidenceAsInterference As System.Boolean
```

```

Dim instance As IInterferenceDetectionMgr
Dim value As System.Boolean
 
instance.TreatCoincidenceAsInterference = value
 
value = instance.TreatCoincidenceAsInterference
```

```

System.bool TreatCoincidenceAsInterference {get; set;}
```

```

property System.bool TreatCoincidenceAsInterference {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to treat coincident entities as interference, false to not

Remarks

Currently, the value set for this property:

- exists only while the InterferenceDetectionMgr object is in scope; i.e., setting this property is temporary.
- does not persist across SOLIDWORKS sessions.
- does not persist into the next invocation of interference detection in the user interface.

Example

[Run Interference Detection (C#)](Run_Interference_Detection_Example_CSharp.htm)  
[Run Interference Detection (VB.NET)](Run_Interference_Detection_Example_VBNET.htm)  
[Run Interference Detection (VBA)](Run_Interference_Detection_Example_VB.htm)  
[Get Interferences Using a Transform (C#)](Detect_Interferences_Using_a_Transform_Example_CSharp.htm)  
[Get Interferences Using a Transform (VB.NET)](Detect_Interferences_Using_a_Transform_Example_VBNET.htm)  
[Get Interferences Using a Transform (VBA)](Detect_Interferences_Using_a_Transform_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IInterferenceDetectionMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr.md)  
[IInterferenceDetectionMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr_members.md)
