# IGetUpperRight Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IGetUpperRight`

Gets the note's upper-right text point.
Gets the note's upper-right text point.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetUpperRight() As System.Double
```

```

Dim instance As INote
Dim value As System.Double
 
value = instance.IGetUpperRight()
```

```

System.double IGetUpperRight()
```

```

System.double IGetUpperRight(); 
```

#### Return Value

- in-process, unmanaged C++: Pointer to an array of doubles (see **Remarks**)
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Format of retval is the following array of 3 doubles:

- return value[0] = x coordinate of upper-right text point
- return value[1] = y coordinate of upper-right text point
- return value[2] = z coordinate of upper-right text point

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[INote Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.md)  
[INote Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote_members.md)  
[INote::GetUpperRight Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetUpperRight.md)
