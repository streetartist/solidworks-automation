# GetMates Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetMates`

Gets the mates for this component.
Gets the mates for this component.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetMates() As System.Object
```

```

Dim instance As IComponent2
Dim value As System.Object
 
value = instance.GetMates()
```

```

System.object GetMates()
```

```

System.Object^ GetMates(); 
```

#### Return Value

Array of mates (either [IMate2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2.md) objects or [IMateInPlace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateInPlace.md) objects)

Remarks

This method eliminates iterating through the list of mates, which can adversely affect performance when the list of mates is long.

Example

[Get Mates (VB.NET)](Get_Mates_Example_VBNET.htm)  
[Get Mates (VBA)](Get_Mates_Example_VB.htm)  
[Get Mates (C#)](Get_Mates_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)  
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.md)
