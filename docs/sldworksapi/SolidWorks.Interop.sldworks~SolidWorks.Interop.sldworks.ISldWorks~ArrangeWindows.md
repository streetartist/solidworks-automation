# ArrangeWindows Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ArrangeWindows`

Arranges the open windows in SOLIDWORKS.
Arranges the open windows in SOLIDWORKS.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub ArrangeWindows( _
   ByVal Style As System.Integer _
) 
```

```

Dim instance As ISldWorks
Dim Style As System.Integer
 
instance.ArrangeWindows(Style)
```

```

void ArrangeWindows( 
   System.int Style
)
```

```

void ArrangeWindows( 
   System.int Style
) 
```

#### Parameters

*Style*
:   Type of arrangement where:

    - 0 = Cascade
    - 1 = Tile horizontally
    - 2 = Tile vertically

Example

[Access Assembly (C++)](Access_Assembly_Example_CPlusPlus_COM.htm)  
[Create and Arrange Windows (VBA)](Create_and_Arrange_Windows_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)  
[ISldWorks::CreateNewWindow Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~CreateNewWindow.md)
