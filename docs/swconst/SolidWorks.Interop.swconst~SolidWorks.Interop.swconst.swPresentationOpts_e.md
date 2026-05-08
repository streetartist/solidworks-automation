# swPresentationOpts_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swPresentationOpts_e`

SOLIDWORKS Presentation options. Bitmask.
SOLIDWORKS Presentation options. [Bitmask](sldworksapiprogguide.chm::/overview/bitmasks.htm).

Syntax

- [Visual Basic](#Syntax-VBAll)
- [C#](#Syntax-CS)
- [Delphi](#Syntax-Delphi)
- [JScript](#Syntax-JScript)
- [Managed Extensions for C++](#Syntax-CPP)
- [C++/CLI](#Syntax-CPP2005)

```

'Declaration
 
```

```

<System.Runtime.InteropServices.GuidAttribute("A08E6606-5F16-4066-9E36-3BD293A42326")>
Public Enum swPresentationOpts_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swPresentationOpts_e
```

```

[System.Runtime.InteropServices.Guid("A08E6606-5F16-4066-9E36-3BD293A42326")]
public enum swPresentationOpts_e : System.Enum 
```

```

public enum swPresentationOpts_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("A08E6606-5F16-4066-9E36-3BD293A42326")
public enum swPresentationOpts_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("A08E6606-5F16-4066-9E36-3BD293A42326")]
__value public enum swPresentationOpts_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("A08E6606-5F16-4066-9E36-3BD293A42326")]
public enum class swPresentationOpts_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swPresentationOpts\_ActiveView** | 32 or 0x20 |
| **swPresentationOpts\_Animations** | 4 or 0x4 |
| **swPresentationOpts\_BackView** | 2048 or 0x800 |
| **swPresentationOpts\_BottomView** | 128 or 0x80 |
| **swPresentationOpts\_CameraMovement** | 16 or 0x10 |
| **swPresentationOpts\_ChkOpenPassword3DPDF** | 1073741824 or 0x40000000; |
| **swPresentationOpts\_CompressTesselation** | 8388608 or 0x800000 |
| **swPresentationOpts\_CreateAttachSTEP242** | 262144 or 0x40000 |
| **swPresentationOpts\_DimetricView** | 32768 or 0x8000 |
| **swPresentationOpts\_DisableCopying3DPDF** | 67108864 or 0x4000000 |
| **swPresentationOpts\_DisableEditing3DPDF** | 33554432 or 0x2000000 |
| **swPresentationOpts\_DisablePrinting3DPDF** | 16777216 or 0x1000000 |
| **swPresentationOpts\_ExcludeFromAnnoView** | 131072 or 0x20000 |
| **swPresentationOpts\_Explodes** | 8 or 0x8 |
| **swPresentationOpts\_FrontView** | 1024 or 0x400 |
| **swPresentationOpts\_HighAccuracy** | 1048576 or 0x100000 |
| **swPresentationOpts\_IsometricView** | 8192 or 0x2000 |
| **swPresentationOpts\_LeftView** | 256 or 0x100 |
| **swPresentationOpts\_LowAccuracy** | 524288 or 0x80000 |
| **swPresentationOpts\_MaxAccuracy** | 4194304 or 0x400000 |
| **swPresentationOpts\_MedAccuracy** | 2097152 or 0x200000 |
| **swPresentationOpts\_None** | 0 or 0x0 |
| **swPresentationOpts\_NormalView** | 4096 or 0x1000 |
| **swPresentationOpts\_OpenPDF** | 65536 or 0x10000 |
| **swPresentationOpts\_PDFPreview** | 268435456 or 0x10000000 |
| **swPresentationOpts\_Pres** | 1 or 0x1 |
| **swPresentationOpts\_RightView** | 512 or 0x200 |
| **swPresentationOpts\_ShowOnlyGraphicalData** | 134217728 or 0x8000000 |
| **swPresentationOpts\_SingleHTML** | 536870912 or 0x20000000; Option to export HTML from 3DPDF |
| **swPresentationOpts\_TopView** | 64 or 0x40 |
| **swPresentationOpts\_TrimetricView** | 16384 or 0x4000 |
| **swPresentationOpts\_U3D** | 2 or 0x2 |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swPresentationOpts\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
