# ViewDisplayFaceted Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ViewDisplayFaceted`

Sets the current display mode to show the facets that make up a shaded picture of STL output.
Sets the current display mode to show the facets that make up a shaded picture of STL output.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub ViewDisplayFaceted() 
```

```

Dim instance As IModelDoc2
 
instance.ViewDisplayFaceted()
```

```

void ViewDisplayFaceted()
```

```

void ViewDisplayFaceted(); 
```

Example

Option Explicit

Sub main()

    Dim swApp                           As SldWorks.SldWorks

    Dim swModel                         As SldWorks.ModelDoc2

    Set swApp = Application.SldWorks

    Set swModel = swApp.ActiveDoc

    swModel.ViewDisplayFaceted

End Sub

Example

[Display Hidden Lines (VBA)](Display_Hidden_Lines_Example_VB.htm)  
[Display Hidden Lines (VB.NET)](Display_Hidden_Lines_Example_VBNET.htm)  
[Display Hidden Lines (C#)](Display_Hidden_Lines_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)
