# CheckClearanceBetween Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClearanceVerificationMgr~CheckClearanceBetween`

Gets or sets the type of clearance check: between selected items or between selected items and the rest of the assembly.
Gets or sets the type of clearance check: between selected items or between selected items and the rest of the assembly.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property CheckClearanceBetween As System.Integer
```

```

Dim instance As IClearanceVerificationMgr
Dim value As System.Integer
 
instance.CheckClearanceBetween = value
 
value = instance.CheckClearanceBetween
```

```

System.int CheckClearanceBetween {get; set;}
```

```

property System.int CheckClearanceBetween {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Type of clearance check as defined by [swCheckClearanceBetween\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCheckClearanceBetween_e.html)

Example

See the [IClearanceVerificationMgr](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClearanceVerificationMgr.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IClearanceVerificationMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClearanceVerificationMgr.md)  
[IClearanceVerificationMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClearanceVerificationMgr_members.md)
