# TreatSubAssembliesAsComponents Property (IClearanceVerificationMgr)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClearanceVerificationMgr~TreatSubAssembliesAsComponents`

Gets or sets whether to treat subassemblies as single components for clearance verification.
Gets or sets whether to treat subassemblies as single components for clearance verification.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property TreatSubAssembliesAsComponents As System.Boolean
```

```

Dim instance As IClearanceVerificationMgr
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

True to not check clearances between components within subassemblies, false to check them

Example

See the [IClearanceVerificationMgr](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClearanceVerificationMgr.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IClearanceVerificationMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClearanceVerificationMgr.md)  
[IClearanceVerificationMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClearanceVerificationMgr_members.md)
