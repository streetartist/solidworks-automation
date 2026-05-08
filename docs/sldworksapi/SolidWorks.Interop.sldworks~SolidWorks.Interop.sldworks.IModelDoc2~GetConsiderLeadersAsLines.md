# GetConsiderLeadersAsLines Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetConsiderLeadersAsLines`

Gets whether the display data of a leader is included as lines when the lines are retrieved from a view or annotation in this document.
Gets whether the display data of a leader is included as lines when the lines are retrieved from a view or annotation in this document.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetConsiderLeadersAsLines() As System.Boolean
```

```

Dim instance As IModelDoc2
Dim value As System.Boolean
 
value = instance.GetConsiderLeadersAsLines()
```

```

System.bool GetConsiderLeadersAsLines()
```

```

System.bool GetConsiderLeadersAsLines(); 
```

#### Return Value

True if leaders are returned as line data, false if leaders are not returned as line data

Remarks

The various GetLeaderCount and GetLeaderAtIndex mehtods return information about where the vertices of the leader are located. These methods also return the leader information as part of its line information.

Depending on what your program is trying to accomplish and which APIs it is using, this duplication of information may not be desirable. [IModelDoc2::SetConsiderLeadersAsLines](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetConsiderLeadersAsLines.md) controls this behavior by setting a flag on the document that indicates whether the leader information should be returned as part of the line information. IModelDoc2::GetConsiderLeadersAsLines gets the current behavior for this document.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)
