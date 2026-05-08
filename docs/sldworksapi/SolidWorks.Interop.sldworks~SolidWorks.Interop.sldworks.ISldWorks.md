# ISldWorks Interface

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks`

Provides direct and indirect access to all other interfaces exposed in the SOLIDWORKS API.
Provides direct and indirect access to all other interfaces exposed in the SOLIDWORKS API.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Interface ISldWorks 
```

```

Dim instance As ISldWorks
```

```

public interface ISldWorks 
```

```

public interface class ISldWorks 
```

Remarks

This interface is the highest-level object in the SOLIDWORKS API. This interface provides a general set of functions that allow application-level operations such as create, open, close, and quit documents, arrange icons and windows, change the active document, and create attribute definitions.

Use CreateObject, GetObject, New, or similar functions to obtain the ISldWorks object from a Dispatch application (Visual Basic or C++ Dispatch). Standalone .exe C++ COM applications can use CoCreateInstance. All of the SOLIDWORKS API add-in wizards automatically create the ISldWorks object for you.

Events are implemented with delegates in the Microsoft .NET Framework. See the [Overview](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md) topic for a list of delegates for this interface.

Example

[Get Spline Points (C++)](Get_Spline_Points_Example_CPlusPlus_COM.htm)  
[Get Names of Creators of Features (C++)](Get_Names_of_Creators_of_Features_Examples_CPlusCPlus_COM.htm)  
[Traverse Bodies (C++)](Traverse_Bodies_Example_CPlusPlusCLI.htm)  
[Manage Drawing Document Line Styles (C#)](Manage_Drawing_Document_Line_Styles_Example_CSharp.htm)  
[Manage Drawing Document Line Styles (VB.NET)](Manage_Drawing_Document_Line_Styles_Example_VBNET.htm)  
[Manage Drawing Document Line Styles (VBA)](Manage_Drawing_Document_Line_Styles_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)  
[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.md)  
[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.md)  
[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.md)
