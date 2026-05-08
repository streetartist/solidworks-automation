# UseTransform Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~UseTransform`

Gets or sets whether to use transforms in interference detection.
Gets or sets whether to use transforms in interference detection.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property UseTransform As System.Boolean
```

```

Dim instance As IInterferenceDetectionMgr
Dim value As System.Boolean
 
instance.UseTransform = value
 
value = instance.UseTransform
```

```

System.bool UseTransform {get; set;}
```

```

property System.bool UseTransform {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to use transforms, false to not

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
