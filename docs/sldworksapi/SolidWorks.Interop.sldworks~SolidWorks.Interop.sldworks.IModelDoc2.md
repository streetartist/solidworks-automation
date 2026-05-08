# IModelDoc2 Interface

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2`

Allows access to SOLIDWORKS documents: parts, assemblies, and drawings.
Allows access to SOLIDWORKS documents: parts, assemblies, and drawings.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Interface IModelDoc2 
```

```

Dim instance As IModelDoc2
```

```

public interface IModelDoc2 
```

```

public interface class IModelDoc2 
```

Remarks

There are three main SOLIDWORKS document types:

- parts
- assemblies
- drawings

Each document type has its own object ([IPartDoc](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.md), [IAssemblyDoc](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.md), and [IDrawingDoc](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.md)) with its own set of related functions. For example, the [IAssemblyDoc::AddComponent4](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~AddComponent4.md) method exists on the IAssemblyDoc object because adding components is specific to assembly documents.

The SOLIDWORKS API also has functions that are common to all document types. For example, printing, saving, or determining the file name associated with a document would be common operations. To expose common document-level functions, the SOLIDWORKS API uses the IModelDoc2 object.

Example

[Traverse Bodies (C++)](Traverse_Bodies_Example_CPlusPlusCLI.htm)  
[Get Names of Creators of Features (C++)](Get_Names_of_Creators_of_Features_Examples_CPlusCPlus_COM.htm)  
[Get Spline Points (C++)](Get_Spline_Points_Example_CPlusPlus_COM.htm)  
[Create Equation-driven Curve (C#)](Create_Equation-driven_Curve_Example_CSharp.htm)  
[Create Equation-driven Curve (VB.NET)](Create_Equation-driven_Curve_Example_VBNET.htm)  
[Create Equation-driven Curve (VBA)](Create_Extruded_Thin_Feature_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
