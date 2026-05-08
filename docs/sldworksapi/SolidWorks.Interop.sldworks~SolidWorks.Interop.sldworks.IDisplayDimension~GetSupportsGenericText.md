# GetSupportsGenericText Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetSupportsGenericText`

Gets whether the display dimension was created in SOLIDWORKS 2011 or later, which, if so, indicates that the display dimension is generic text.
Gets whether the display dimension was created in SOLIDWORKS 2011 or later, which, if so, indicates that the display dimension is generic text.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetSupportsGenericText() As System.Boolean
```

```

Dim instance As IDisplayDimension
Dim value As System.Boolean
 
value = instance.GetSupportsGenericText()
```

```

System.bool GetSupportsGenericText()
```

```

System.bool GetSupportsGenericText(); 
```

#### Return Value

True if the display dimension was created in SOLIDWORKS 2011 or later and is generic text, false if the display dimension was created in an earlier release of SOLIDWORKS and is dimension text

Example

[Get SOLIDWORKS Version of Display Dimension (C#)](Get_SOLIDWORKS_Version_of_Display_Dimension_Example_CSharp.htm)  
[Get SOLIDWORKS Version of Display Dimension (VB.NET)](Get_SOLIDWORKS_Version_of_Display_Dimension_Example_VBNET.htm)  
[Get SOLIDWORKS Version of Display Dimension (VBA)](Get_SOLIDWORKS_Version_of_Display_Dimension_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.md)  
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.md)
