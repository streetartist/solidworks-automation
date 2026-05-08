# InsertLoadReference Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~InsertLoadReference`

Creates a mate load reference to the specified or selected mate.
Creates a mate load reference to the specified or selected mate.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertLoadReference( _
   ByVal Mate As Mate2 _
) As MateLoadReference
```

```

Dim instance As IAssemblyDoc
Dim Mate As Mate2
Dim value As MateLoadReference
 
value = instance.InsertLoadReference(Mate)
```

```

MateLoadReference InsertLoadReference( 
   Mate2 Mate
)
```

```

MateLoadReference^ InsertLoadReference( 
   Mate2^ Mate
) 
```

#### Parameters

*Mate*
:   [Mate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2.md) to which to add a mate load reference; if NULL passed in, then the mate must already be selected

#### Return Value

[IMateLoadReference](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateLoadReference.md)

Remarks

The supplemental faces for the mate load reference must be selected before using this method. SOLIDWORKS determines which components own the selected supplemental faces and matches them to the components associated with the specified or selected mate. If the component of a selected supplemental face does not match either of the components of the mate, then that face is ignored.

This method rebuilds the FeatureManager design tree, which can be a time-consuming operation if the FeatureManage design tree is large. If using this method to add many load references at once, use [IFeatureManager::EnableFeatureTree](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~EnableFeatureTree.md) before and after using IAssemblyDoc::InsertLoadReference to disable and then re-enable rebuilding the FeatureManager design tree.

Example

[Insert Mate Load Reference (C#)](Insert_Mate_Load_Reference_Example_CSharp.htm)  
[Insert Mate Load Reference (VB.NET)](Insert_Mate_Load_Reference_Example_VBNET.htm)  
[Insert Mate Load Reference (VBA)](Insert_Mate_Load_Reference_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.md)  
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.md)
