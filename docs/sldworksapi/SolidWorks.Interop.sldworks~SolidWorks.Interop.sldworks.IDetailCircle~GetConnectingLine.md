# GetConnectingLine Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle~GetConnectingLine`

Gets the end point coordinates of the connecting line for this detail circle.
Gets the end point coordinates of the connecting line for this detail circle.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetConnectingLine() As System.Object
```

```

Dim instance As IDetailCircle
Dim value As System.Object
 
value = instance.GetConnectingLine()
```

```

System.object GetConnectingLine()
```

```

System.Object^ GetConnectingLine(); 
```

#### Return Value

Array (see **Remarks**)

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
[IDetailCircle::IGetConnectingLine Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle~IGetConnectingLine.md)
