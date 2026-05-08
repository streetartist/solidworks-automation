# CreateFastenersFolder Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~CreateFastenersFolder`

Gets or sets whether to create the Fasteners folders to segregate interferences involving fasteners.
Gets or sets whether to create the Fasteners folders to segregate interferences involving fasteners.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property CreateFastenersFolder As System.Boolean
```

```

Dim instance As IInterferenceDetectionMgr
Dim value As System.Boolean
 
instance.CreateFastenersFolder = value
 
value = instance.CreateFastenersFolder
```

```

System.bool CreateFastenersFolder {get; set;}
```

```

property System.bool CreateFastenersFolder {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to create fasteners folder, false to not

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
[IInterference::IsFastener Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterference~IsFastener.md)
