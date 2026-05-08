# GetSustainability Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetSustainability`

Gets the entry-point interface to the SOLIDWORKS Sustainability API.
Gets the entry-point interface to the SOLIDWORKS Sustainability API.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetSustainability() As System.Object
```

```

Dim instance As IModelDocExtension
Dim value As System.Object
 
value = instance.GetSustainability()
```

```

System.object GetSustainability()
```

```

System.Object^ GetSustainability(); 
```

#### Return Value

[ISustainabilityApp](SOLIDWORKS.Interop.sustainability~SOLIDWORKS.Interop.sustainability.ISustainabilityApp.md)

Remarks

SOLIDWORKS Sustainability and its API are only available in SOLIDWORKS Professional and SOLIDWORKS Premium.

Example

[Calculate Environmental Impact of Part (VBA)](Calculate_Environmental_Impact_of_Part_Example_VB.htm)  
[Calculate Environmental Impact of Part (VB.NET)](Calculate_Environmental_Impact_of_Part_Example_VBNET.htm)  
[Calculate Environmental Impact of Part (C#)](Calculate_Environmental_Impact_of_Part_Example_CSharp.htm)  
[Calculate Environmental Impact of Assembly (VBA)](Calculate_Environmental_Impact_of_Assembly_Example_VB.htm)  
[Calculate Environmental Impact of Assembly (VB.NET)](Calculate_Environmental_Impact_of_Assembly_Example_VBNET.htm)  
[Calculate Environmental Impact of Assembly (C#)](Calculate_Environmental_Impact_of_Assembly_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)
