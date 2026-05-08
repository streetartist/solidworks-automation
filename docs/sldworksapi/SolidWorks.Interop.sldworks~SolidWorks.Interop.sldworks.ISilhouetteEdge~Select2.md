# Select2 Method (ISilhouetteEdge)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISilhouetteEdge~Select2`

Selects the silhouette edge in the active drawing view.
Selects the silhouette edge in the active drawing view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function Select2( _
   ByVal Append As System.Boolean, _
   ByVal Data As SelectData _
) As System.Boolean
```

```

Dim instance As ISilhouetteEdge
Dim Append As System.Boolean
Dim Data As SelectData
Dim value As System.Boolean
 
value = instance.Select2(Append, Data)
```

```

System.bool Select2( 
   System.bool Append,
   SelectData Data
)
```

```

System.bool Select2( 
   System.bool Append,
   SelectData^ Data
) 
```

#### Parameters

*Append*
:   True appends this selection to the selection list, false replaces the selection list with this selection

*Data*
:   [SelectData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectData.md) object

#### Return Value

True if the selection is successful, false if not

Example

[Select Silhouette Edge Attached to Note (C#)](Select_Silhouette_Edge_Attached_to_Note_Example_CSharp.htm)  
[Select Silhouette Edge Attached to Note (VB.NET)](Select_Silhouette_Edge_Attached_to_Note_Example_VBNET.htm)  
[Select Silhouette Edge Attached to Note (VBA)](Select_Silhouette_Edge_Attached_to_Note_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISilhouetteEdge Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISilhouetteEdge.md)  
[ISilhouetteEdge Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISilhouetteEdge_members.md)
