# IGetConnectingLine Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle~IGetConnectingLine`

Gets the end point coordinates of the connecting line
Gets the end point coordinates of the connecting line

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetConnectingLine() As System.Double
```

```

Dim instance As IDetailCircle
Dim value As System.Double
 
value = instance.IGetConnectingLine()
```

```

System.double IGetConnectingLine()
```

```

System.double IGetConnectingLine(); 
```

#### Return Value

- in-process, unmanaged C++: Pointer to an array of 6 doubles (see **Remarks**)

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

This is only valid if there is a connecting line. Use [IDetailCircle::GetStyle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle~GetStyle.md) to determine if this detail circle is valid for this command.

|  |  |
| --- | --- |
| retval[0] | X-coordinate of first connecting line point |
| retval[1] | Y-coordinate of first connecting line point |
| retval[2] | Z-coordinate of first connecting line point |
| retval[3] | X-coordinate of second connecting line point |
| retval[4] | Y-coordinate of second connecting line point |
| retval[5] | Z-coordinate of second connecting line point |

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDetailCircle Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle.md)  
[IDetailCircle Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle_members.md)  
[IDetailCircle::GetConnectingLine Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle~GetConnectingLine.md)
