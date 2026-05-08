# swLeaderStyle_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swLeaderStyle_e`

Leader styles.
Leader styles.

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

<System.Runtime.InteropServices.GuidAttribute("72D1641A-F5BC-4A9A-9FE3-C06722EA7EF4")>
Public Enum swLeaderStyle_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swLeaderStyle_e
```

```

[System.Runtime.InteropServices.Guid("72D1641A-F5BC-4A9A-9FE3-C06722EA7EF4")]
public enum swLeaderStyle_e : System.Enum 
```

```

public enum swLeaderStyle_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("72D1641A-F5BC-4A9A-9FE3-C06722EA7EF4")
public enum swLeaderStyle_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("72D1641A-F5BC-4A9A-9FE3-C06722EA7EF4")]
__value public enum swLeaderStyle_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("72D1641A-F5BC-4A9A-9FE3-C06722EA7EF4")]
public enum class swLeaderStyle_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swAlwaysAttachToBalloon** | 0x1004 or 4100 = [Bitmask](sldworksapiprogguide.chm::/overview/bitmasks.htm); applies only to balloon annotations; specifies that the balloon's **Always Attach to Balloon** leader option is enabled and the leader is always attached to the balloon when quantity is specified, and the balloon's **Break Around** leader option is disabled; if not specified, then the balloon's **Always Attach to Balloon** leader option is disabled, and the balloon's **Break Around** leader option is enabled and the balloon's leader is set to break around quantity; AND with one of the following options:   - swBENT - swSTRAIGHT - swUNDERLINED (parts only) - swSPLINE (drawings only) - swVDA |
| **swAttachLeaderBottom** | 0x400 or 1024 = Bitmask; in part's multiline note, attaches leader to bottom of note; AND with one of the following options:   - swBENT - swSTRAIGHT - swUNDERLINED |
| **swAttachLeaderCenter** | 0x200 or 512 = Bitmask; in a part's multiline note, attaches leader to center of note; AND with one of the following options:   - swBENT - swSTRAIGHT - swUNDERLINED |
| **swAttachLeaderNearest** | 0x800 or 2048 = Bitmask; in a part's multiline note, left leader attaches to the top of note and right leader attaches to the bottom of note; AND with one of the following options:   - swBENT - swSTRAIGHT - swUNDERLINED |
| **swAttachLeaderTop** | 0x100 or 256 = Bitmask; in a part's multiline note, attaches leader to top of note; AND with one of the following options:   - swBENT - swSTRAIGHT - swUNDERLINED |
| **swBENT** | 2 = Creates a bent leader |
| **swNO\_LEADER** | 0 = No leader |
| **swSPLINE** | 4 = Creates a spline leader from a note; for drawings only |
| **swSTRAIGHT** | 1 = Creates a straight leader |
| **swUNDERLINED** | 3 = Creates an underlined leader; for parts only |
| **swVDA** | 8 = Creates an inspection leader |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swLeaderStyle\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
