# IEntity Interface

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity`

Allows access to an attribute instance that is stored on an entity.
Allows access to an attribute instance that is stored on an entity.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Interface IEntity 
```

```

Dim instance As IEntity
```

```

public interface IEntity 
```

```

public interface class IEntity 
```

Remarks

In Microsoft Visual Studio 2008/MFC 9.0 or later, Microsoft added a new interface called IEntity. Your add-in might not compile if it uses both this interface and the SOLIDWORKS IEntity interface.

Possible errors are:

- error C3121: cannot change GUID for class 'IEntity'
- error C2011: 'IEntity' : 'struct' type redefinition
- undefined symbol errors when linking add-ins that do a QueryInterface on IEntity

To avoid errors, you can:

- Include the namespace when declaring an IEntity variable:

SldWorks::IEntity ent

- Rename IEntity by adding the rename function to the import of **sldworks.tlb**:  
      #import "sldworks.tlb" rename("IEntity", "SWEntity")

     and do any of the following:

- use SWEntity instead of IEntity in your code
- do a QueryInterface using the GUID constant of the renamed interface:

pFace->QueryInterface(**IID\_SWEntity**, (LPVOID\*)&entity);

- do a QueryInterface using a GUID lookup of the renamed interface:

pFace->QueryInterface**(\_\_uuidof(SWEntity),** (LPVOID\*)&entity);

Example

[Get Offset Surface Data (C#)](Get_Offset_Surface_Data_Example_CSharp.htm)  
[Get Offset Surface Data (VB.NET)](Get_Offset_Surface_Data_Example_VBNET.htm)  
[Get Offset Surface Data (VBA)](Get_Offset_Surface_Data_Example_VB.htm)  
[Select Edges of All Holes on Face (C#)](Select_Edges_of_All_Holes_on_Face_Example_CSharp.htm)  
[Select Edges of All Holes on Face (VB.NET)](Select_Edges_of_All_Holes_on_Face_Example_VBNET.htm)  
[Select Edges of All Holes on Face (VBA)](Select_Edges_of_All_Holes_on_Face_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IEntity Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity_members.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
