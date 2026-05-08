# MergeBendTags Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~MergeBendTags`

Merges or unmerges bend tags in drawings of sheet metal parts.
Merges or unmerges bend tags in drawings of sheet metal parts.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function MergeBendTags( _
   ByVal Merge As System.Boolean, _
   ByVal BendNotes As System.Object _
) As System.Boolean
```

```

Dim instance As IView
Dim Merge As System.Boolean
Dim BendNotes As System.Object
Dim value As System.Boolean
 
value = instance.MergeBendTags(Merge, BendNotes)
```

```

System.bool MergeBendTags( 
   System.bool Merge,
   System.object BendNotes
)
```

```

System.bool MergeBendTags( 
   System.bool Merge,
   System.Object^ BendNotes
) 
```

#### Parameters

*Merge*
:   True to merge bend tags, false to unmerge a merged bend tag

*BendNotes*
:   Array of two or more bend [tags](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.md) to merge or an array of one merged bend tag to unmerge

#### Return Value

True if the bend tags are merged or a merged bend tag is unmerged, false if not

Remarks

|  |  |
| --- | --- |
| **To...** | **Do...** |
| Merge two or more bend tags | 1. Select the bend tags to merge. 2. Select the drawing view in which the bend tags exist. 3. Call this method with the Merge parameter set to true. 4. Rebuild the drawing. |
| Unmerge a merged bend tag | 1. Select the drawing view in which the merged bend tag exists. 2. Activate the drawing view in which the merged bend tag exists. 3. Select the merged bend tag to unmerge. 4. Call this method with the Merge parameter set to false. |

Example

[Merge and Unmerge Bend Tags (C#)](Merge_and_Unmerge_Bend_Tags_Example_CSharp.htm)  
[Merge and Unmerge Bend Tags (VB.NET)](Merge_and_Unmerge_Bend_Tags_Example_VBNET.htm)  
[Merge and Unmerge Bend Tags (VBA)](Merge_and_Unmerge_Bend_Tags_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[INote::IsBendLineNote Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IsBendLineNote.md)
