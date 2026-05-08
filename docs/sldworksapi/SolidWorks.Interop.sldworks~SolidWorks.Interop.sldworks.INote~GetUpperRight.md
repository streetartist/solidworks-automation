# GetUpperRight Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetUpperRight`

Gets the note's upper-right text point.
Gets the note's upper-right text point.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetUpperRight() As System.Object
```

```

Dim instance As INote
Dim value As System.Object
 
value = instance.GetUpperRight()
```

```

System.object GetUpperRight()
```

```

System.Object^ GetUpperRight(); 
```

#### Return Value

Array of doubles (see **Remarks**)

Remarks

Format of retval is the following array of 3 doubles:

- return value[0] = x coordinate of upper-right text point
- return value[1] = y coordinate of upper-right text point
- return value[2] = z coordinate of upper-right text point

Example

[Get Upper-right Text Coordinates of Selected Note (VBA)](Get_Upper-right_Text_Coordinates_of_Selected_Note_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[INote Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.md)  
[INote Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote_members.md)  
[INote::IGetUpperRight Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IGetUpperRight.md)
