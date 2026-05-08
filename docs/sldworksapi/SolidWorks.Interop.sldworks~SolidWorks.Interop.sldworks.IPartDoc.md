# IPartDoc Interface

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc`

Provides access to functions that perform operations on parts in part documents.
Provides access to functions that perform operations on parts in part documents.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Interface IPartDoc 
```

```

Dim instance As IPartDoc
```

```

public interface IPartDoc 
```

```

public interface class IPartDoc 
```

Remarks

This interface provides functions that allow you to:

- create bodies and features.
- perform suppress operations.
- obtain part extents and tessellation.
- locate entities by name.

The SOLIDWORKS API also has functions that are common to all document types. For example, determining the file name associated with a document would be a common operation. To expose common document-level functions, the SOLIDWORKS API uses the [IModelDoc2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md) object.

Events are implemented with delegates in the Microsoft .NET Framework. See the [Overview](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md) topic for a list of delegates for this interface.

Example

[Get Sketches (C++)](Get_Sketches_Example_CPlusPlus_COM.htm)  
[Traverse Bodies (C++)](Traverse_Bodies_Example_CPlusPlusCLI.htm)  
[Create Imported Surface Body From Sketch (C#)](Create_Imported_Surface_Body_from_Sketch_Example_CSharp.htm)  
[Get Differences Between Parts (VBA)](Get_Differences_Between_Parts_Example_VB.htm)  
[Import Step File (C#)](Import_STEP_File_Example_CSharp.htm)  
[Import Step File (VB.NET)](Import_STEP_File_Example_VBNET.htm)  
[Import Step File (VBA)](Import_STEP_File_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
