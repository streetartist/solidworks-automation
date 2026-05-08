# GetComponentByID Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetComponentByID`

Gets a top-level assembly component using its component ID.
Gets a top-level assembly component using its component ID.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetComponentByID( _
   ByVal ID As System.Integer _
) As System.Object
```

```

Dim instance As IAssemblyDoc
Dim ID As System.Integer
Dim value As System.Object
 
value = instance.GetComponentByID(ID)
```

```

System.object GetComponentByID( 
   System.int ID
)
```

```

System.Object^ GetComponentByID( 
   System.int ID
) 
```

#### Parameters

*ID*
:   Component ID of top-level assembly component (see **Remarks**)

#### Return Value

Top-level [component](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)

Remarks

Call [IComponent2::GetID](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetID.md) before calling this method to get the component ID of the top-level assembly component to pass to this method.

Example

[Get Top-level Components Using Component IDs (C#)](Get_Top-level_Component_Using_Component_IDs_Example_CSharp.htm)  
[Get Top-level Components Using Component IDs (VB.NET)](Get_Top-level_Component_Using_Component_IDs_Example_VBNET.htm)  
[Get Top-level Components Using Component IDs (VBA)](Get_Top-level_Component_Using_Component_IDs_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.md)  
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.md)  
[IAssemblyDoc::GetComponentByName Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetComponentByName.md)  
[IAssemblyDoc::GetComponents Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetComponents.md)  
[IAssemblyDoc::IGetComponents Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~IGetComponents.md)
